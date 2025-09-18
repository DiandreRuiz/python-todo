def display_user_error(message) -> str:
    """Wraps error message in ASCII to make text red & prints"""
    print(
        f"""
        ________________________
        
        \033[91m{message}\033[0m
        ________________________
    
    """
    )


def display_success(message) -> str:
    """Wraps success message in ASCII to make text green & prints"""
    print(
        f"""
        ________________________
        
        \033[92m{message}\033[0m
        ________________________
    
    """
    )