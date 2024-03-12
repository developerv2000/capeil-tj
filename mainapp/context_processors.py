from categories.models import Category


def template_based(request):
    data = {}

    # Determine the current template name
    template_name = None
    if hasattr(request, 'resolver_match'):
        template_name = request.resolver_match.view_name
        # template_name = template_name.replace(':', '/') + '.html' # Convert template name to match format

        # Share data based on rendered template
        match template_name:
            case 'quotes:index':
                data['aside_categories'] = Category.objects.all()

    return data
