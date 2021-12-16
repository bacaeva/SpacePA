from django.forms import modelformset_factory
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
# from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from product.forms import ProductForm, ProductImageForm
from product.models import Product, ProductImage


# def products_list(request):
#     products = Product.objects.all()
#     context = {'products': products}
#     return render(request, 'product/products_list.html', context)



# class ProductsListView(View):
#     def get(self,request):
#         products = Product.objects.all()
#         context = {'products': products}
#         return render(request, 'product/products_list.html', context)



class ProductsListsView(ListView):
    queryset = Product.objects.all()
    template_name = 'product/main.html'
    context_object_name = 'products'


class ProductDetailsView(DetailView):
    queryset = Product.objects.all()
    template_name = 'product/product_details.html'
    context_object_name = 'product'



class CreateProductView(CreateView):
    queryset = Product.objects.all()
    template_name = 'product/create_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('products-list')

    def post(self, request, *args, **kwargs):
        self.object = None
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            for image in request.FILES.getlist('product_image'):
                ProductImage.objects.create(product=product, image=image)
            return redirect(reverse_lazy('product-details', args=(product.id, )))
        return self.form_invalid(form)


class UpdateProductView(UpdateView):
    queryset = Product.objects.all()
    form_class = ProductForm
    template_name='product/update_product.html'
    context_object_name = 'product'


class DeleteProductView(DeleteView):
    queryset = Product.objects.all()
    template_name = 'product/delete_product.html'
    success_url = reverse_lazy('products-list')



        # return redirect(reverse_lazy('create-product'))

# ImagesFormSet=modelformset_factory(ProductImage,
#                                            form=ProductImageForm,
#                                            extra=3,
#                                            max_num = 4,
#                                            can_delete=True)


# class CreateProductView(CreateView):
#     queryset = Product.objects.all()
#     template_name = 'product/create_product.html'
#     form_class = ProductForm
#     success_url = reverse_lazy('products-list')
#
#     # def get_context_data(self, **kwargs):
#     #     context = super().get_context_data()
#     #
#     #     context['images_formset']= ImagesFormSet(queryset = ProductImage.objects.none())
#     #     return context
#
#     def post(self, request, *args,**kwargs):
#         form = ProductForm(request.POST)
#         formset = ImagesFormSet(request.POST,
#                              request.FILES,
#                              queryset=ProductImage.objects.none())
#         if form.is_valid() and formset.is_valid():
#             product = form.save()
#             for image_form in formset.cleaned_data:
#                 image = image_form.get('image')
#                 if image:
#                     pie = ProductImage(product=product, image=image)
#                     pie.save()
#                 return redirect(reverse_lazy('product_details', args=(product.id,)))
#


#CRUD(Create, Resrieve, Update,Delete)


# MVC(Model-View-Controller)
# Model(model)
# View (templates)
# Controller-(views)

