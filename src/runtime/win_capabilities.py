def list_audio_devices(self) -> List[AudioDevice]:
    """
    Vráti zoznam audio zariadení pomocou Windows Core Audio API (WASAPI).
    Aktuálne vracia iba predvolené zariadenie (default output).
    """
    try:
        import ctypes
        from ctypes import POINTER
        from ctypes.wintypes import DWORD

        # COM interfaces
        CLSCTX_ALL = 23

        class IMMDeviceEnumerator(ctypes.c_void_p):
            pass

        class IMMDevice(ctypes.c_void_p):
            pass

        class IPropertyStore(ctypes.c_void_p):
            pass

        # GUIDs
        CLSID_MMDeviceEnumerator = ctypes.c_char_p(
            b"{BCDE0395-E52F-467C-8E3D-C4579291692E}"
        )
        IID_IMMDeviceEnumerator = ctypes.c_char_p(
            b"{A95664D2-9614-4F35-A746-DE8DB63617E6}"
        )

        # Initialize COM
        ole32 = ctypes.windll.ole32
        ole32.CoInitialize(None)

        enumerator = POINTER(IMMDeviceEnumerator)()
        ole32.CoCreateInstance(
            CLSID_MMDeviceEnumerator,
            None,
            CLSCTX_ALL,
            IID_IMMDeviceEnumerator,
            ctypes.byref(enumerator)
        )

        # Get default audio endpoint (render/output)
        default_device = POINTER(IMMDevice)()
        enumerator.GetDefaultAudioEndpoint(0, 1, ctypes.byref(default_device))

        # Open property store
        property_store = POINTER(IPropertyStore)()
        default_device.OpenPropertyStore(0, ctypes.byref(property_store))

        # PROPERTYKEY struct
        class PROPERTYKEY(ctypes.Structure):
            _fields_ = [
                ("fmtid", ctypes.c_byte * 16),
                ("pid", DWORD),
            ]

        # PKEY_Device_FriendlyName
        PKEY_Device_FriendlyName = PROPERTYKEY(
            (0xA4, 0x41, 0x4F, 0xC6, 0xE4, 0xD8, 0x4A, 0xD1,
             0x87, 0xB6, 0xE0, 0xDB, 0xEF, 0xE3, 0x5A, 0xA5),
            14
        )

        # PROPVARIANT struct
        class PROPVARIANT(ctypes.Structure):
            _fields_ = [
                ("vt", ctypes.c_ushort),
                ("wReserved1", ctypes.c_ubyte),
                ("wReserved2", ctypes.c_ubyte),
                ("wReserved3", DWORD),
                ("pszVal", ctypes.c_wchar_p),
            ]

        prop = PROPVARIANT()
        property_store.GetValue(ctypes.byref(PKEY_Device_FriendlyName), ctypes.byref(prop))

        device_name = prop.pszVal

        return [
            AudioDevice(
                id="default",
                name=device_name,
                is_default=True
            )
        ]

    except Exception as exc:
        log.exception("Failed to list audio devices: %s", exc)
        return []
