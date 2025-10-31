from .app.app import App

def main():
    """CLI entry for packaging tools."""
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()