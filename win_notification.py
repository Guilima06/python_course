from win10toast import ToastNotifier

# Inicializa #
toaster = ToastNotifier()

toaster.show_toast(
    "Notificação",
    "Olá Psycodebr :)",
    threaded=True,
    icon_path=None,
    duration=3  # 3 segundos
)