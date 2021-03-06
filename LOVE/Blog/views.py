from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import(
	CreateView,
	DetailView,
	ListView,
	UpdateView,
	DeleteView,
	View,
	)

from .models import Article
from .forms import ArticleForm

# 有ListView這django內建模組，也不用return render(...)
class ArticleListView(ListView):
	queryset = Article.objects.all()
	template_name = 'blog/article_list.html'
	# 透過這個才能跟前端的樣式網頁做連結

class ArticleDetailView(DetailView):
	# 過濾obj的id > 1的網頁，如果訪客訪問no.1的網頁，就會出現404，page not found。
	# queryset = Article.objects.all()
	template_name = 'blog/article_detail.html'

	# 這個function是DetailView模組內建的函式，而ListView沒有
	# 這個函式的用意是為了讓此url的path('<int:id>')標籤裡頭可以輸入的是"id"。
	# 但我把它改成<int:akb48>，比較不會混淆。
	# 所謂的self，不是網頁實體的物件，而是訪客訪問的request data。
	def get_object(self):
		pk = self.kwargs.get("akb48")
	# 	#這裏kwargs.get("xx")對照url裡path('<int:xx>')
		return get_object_or_404(Article, id=pk)
		# 這裡返回給訪客的是，將一個網址no.對照成物件的no.
		# 實體出來後會到template前端html樣板進行呈現
		# 若沒有對應的no.，就會產生404，page not found.

class ArticleCreateView(CreateView):
	template_name = 'blog/article_create.html'
	form_class = ArticleForm
	
	#
	def form_valid(self, form): # 子類的方法form_valid
		print(form.cleaned_data) # 可在終端機看到驗證後的data
		return super().form_valid(form) 
		# 因為父類的方法form_valid和子類方法同名，前面加個super()來指名要用父類的方法

	# create完物件後，網址立馬跳http://127.0.0.1:8000+"XXX"
	def get_success_url(self):
		return '/blog'


class ArticleUpdateView(UpdateView):
	template_name = 'blog/article_create.html'
	form_class = ArticleForm
	
	# 接收request來的data，從sql撈物件'blog/article_create.html'呈現，但表格內有原本的內容
	# 然後物件重新以不符合id就回傳404
	def get_object(self):
		id = self.kwargs.get("akb48")
	# 	#這裏kwargs.get("xx")對照url裡path('<int:xx>')
		return get_object_or_404(Article, id=id)

	# # self就是ArticleUpdateView(UpdateView)類別本身的實例
	# def form_valid(self, form): # 非必要執行的方法
	# 	print(form.cleaned_data)
	# 	return super().form_valid(form)

	# create完物件後，網址立馬跳http://127.0.0.1:8000+"XXX"
	def get_success_url(self):
		return "/blog"



class ArticleDeleteView(DeleteView):
	# 過濾obj的id > 1的網頁，如果訪客訪問no.1的網頁，就會出現404，page not found。
	# queryset = Article.objects.all()
	template_name = 'blog/article_delete.html'

	def get_object(self):
		id = self.kwargs.get("akb48")
	# 	#這裏kwargs.get("xx")對照url裡path('<int:xx>')
		return get_object_or_404(Article, id=id)

	def get_success_url(self):
		return "/blog"



