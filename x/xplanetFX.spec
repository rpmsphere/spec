Name: xplanetFX
Summary: Render desktop wallpapers of mother earth based on xplanet
Version: 2.6.7
Release: 3.1
Group: Converted/utils
License: see /usr/share/doc/xplanetfx/copyright
URL: https://mein-neues-blog.de/xplanetFX
Source0: https://repository.mein-neues-blog.de:9000/latest/%{name}.tar.gz
BuildArch: noarch

%description
The images are updated regularly by a daemon. It can be controlled
by CLI but also provides a GTK-UI. xplanetFX can be styled with different
templates.

%prep
%setup -q -c
sed -i 's|snafu|$XDG_CURRENT_DESKTOP|' usr/bin/%{name}

%build

%install
mkdir -p %{buildroot}
cp -a usr %{buildroot}

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_datadir}/%{name}/%{name}_* %{buildroot}%{_datadir}/%{name}/stars/catalog.py

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.svg
%{_datadir}/doc/%{name}
%{_datadir}/applications/%{name}.desktop

%changelog
* Wed May 04 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2.6.7
- Rebuilt for Fedora
