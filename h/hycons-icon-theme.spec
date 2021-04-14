%define theme_name Hycons

Summary:        Hycons icon theme
Name:           hycons-icon-theme
Version:        3.0.0
Release:        7.1
License:        CC-BY-NC-SA
Group:          User Interface/Desktops
URL:            http://kde-look.org/content/show.php/Hycons?content=101767
Source0:        Hycons.tar.gz
BuildArch:      noarch

%description
A long time without update this on kde-look :P
Recently I started with a rewrite from 0 of all the icon set.

%prep
%setup -q -n Hycons

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}
cp -a * $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%{_datadir}/icons/%{theme_name}

%changelog
* Wed Aug 01 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 3.0.0
- Rebuilt for Fedora
* Sun Aug 28 2011 Damianator <damianatorrpm@gmail.com> - 3.0.0
- Initial release
