%global mod_name shoes
%global gem_dir %{_datadir}/rubygems
%global __spec_install_post %{nil}

Name:           rubygem-shoes
Version:        3.0.1
Release:        7.1
BuildRequires:  ruby, rubygems, rubypick
BuildArch:      noarch
URL:            http://shoesrb.com/
Source0:        https://rubygems.global.ssl.fastly.net/gems/%{mod_name}-%{version}.gem
Summary:        The best little GUI toolkit for Ruby
License:        MIT
Group:          Development/Languages/Ruby

%description
Shoes is a GUI Toolkit originally developed by the legendary _why.
Shoes is the best little DSL for cross-platform GUI programming there is.
It feels like real Ruby, rather than just another C++ library wrapper.
If Gtk or wxWidgets is Rails, Shoes is Sinatra.

%prep

%build

%install
mkdir -p $RPM_BUILD_ROOT%{gem_dir} $RPM_BUILD_ROOT%{_bindir}
gem install --local --build-root $RPM_BUILD_ROOT --install-dir %{gem_dir} --force --no-document %{SOURCE0}

%files
%{gem_dir}/cache/%{mod_name}-%{version}.gem
%{gem_dir}/gems/%{mod_name}-%{version}
%{gem_dir}/specifications/%{mod_name}-%{version}.gemspec
%if %{fedora}<24
%{gem_dir}/doc/%{mod_name}*
%endif

%changelog
* Fri Jan 16 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 3.0.1
- Rebuilt for Fedora
* Wed Aug 28 2013 benny.gaechter@gmail.com
-Added correct license
* Wed Aug 28 2013 benny.gaechter@gmail.com
-fixed rpmlint errors with rpmlintrc
* Wed Aug 28 2013 benny.gaechter@gmail.com
-Created package for gem 'shoes'
