class Product:
    def __init__(self, title, description, image_url):
        self.title = title
        self.description = description
        self.image_url = image_url

def validate_product(product):
    if len(product.title) > 50:
        raise ValueError("Title is too long! Must be 50 characters or fewer.")
    if len(product.description) > 1000:
        raise ValueError("Description is too long! Must be 1000 characters or fewer.")
    if not product.image_url.startswith('http'):
        raise ValueError("Image URL is not valid!")

def create_social_media_post(product):
    # This will contain the logic for creating the social media post
    # For now, it simply formats a string with the product details
    return f"Check out our new product: {product.title}! {product.image_url}"

def main():
    product = Product("My Cool Product", "This is a really cool product. You should buy it!", "http://mywebsite.com/myproduct.jpg")
    try:
        validate_product(product)
        post = create_social_media_post(product)
        print(post)
    except ValueError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
