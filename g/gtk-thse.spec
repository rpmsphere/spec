%global _name rico_GTK-Theme-Selector

Name: gtk-thse
Summary: A GTK theme switcher
Version: 0.72
Release: 2.1
Source:  https://www.rico-net.de/gtk-thse/tar/%{_name}-%{version}.tar.gz
URL: https://www.rico-net.de/gtk-thse/
License: GPL
Group: GNOME
BuildRequires: gtk+-devel glib-devel

%description 
rico_GTK-Theme-Selector is little application to change the GTK+ Theme.

%prep
%setup -q -n %{_name}-%{version}

%build
make 

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install %{_name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%files
%doc README README.de COPYING AUTHORS CHANGELOG CHANGELOG.de BUGS NEWS THANKS TODO
%{_bindir}/%{name}

%changelog
* Thu Aug 04 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.72
- Rebuilt for Fedora
* Sat Jul 07 2001 Enrico Nemack <rico.ffo@gmx.de> 0.71
- Initial package
