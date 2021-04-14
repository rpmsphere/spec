Name:           deepin-utils
Summary:        Utils library for all project in Linux Deepin
License:        GPL-3.0+
Group:          System/GUI/GNOME
Version:        1.0
Release:        3.1
URL:            https://github.com/linuxdeepin/deepin-utils
Source0:        %{name}-master.zip
BuildRequires:  pkgconfig(cairo) 
BuildRequires:  pkgconfig(pygobject-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  webkitgtk-devel
BuildRequires:  libsoup-devel
BuildRequires:  python-devel
BuildRequires:  pygtk2-devel
BuildRequires:  python-setuptools
Requires:       pywebkitgtk
Requires:       numpy

%description
Utils library for all project in Linux Deepin.

Base code move from utils module of deepin-ui.

%prep
%setup -q -n %{name}-master

%build

%install
export CFLAGS="$RPM_OPT_FLAGS" 
python2 setup.py install --prefix=%{_prefix} --root=$RPM_BUILD_ROOT

%files 
%{python2_sitearch}/deepin_utils
%{python2_sitearch}/deepin_utils-1.0-py2.7.egg-info
%{python2_sitearch}/dtk_cairo_blur.so
%{python2_sitearch}/dtk_webkit_cookie.so
%{python2_sitearch}/deepin_font_icon.so

%changelog
* Wed Nov 29 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuilt for Fedora
* Wed Aug 14 2013 hillwood@linuxfans.org
- update to git20130724
  upsteam did not provide changlog.
* Sun Apr 28 2013 hillwood@linuxfans.org
- update to git20130314
  fix bugs
* Wed Feb  6 2013 hillwood@linuxfans.org
- Initial package
