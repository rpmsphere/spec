%define theme_name ComicFaces

Summary:        Comic Faces cursor theme
Name:           comicfaces-cursor-theme
Version:        0.11
Release:        2.1
License:        LGPL
Group:          User Interface/Desktops
URL:            http://gnome-look.org/content/show.php/ComicFaces?content=161673
Source0:        http://gnome-look.org/CONTENT/content-files/161673-ComicFaces.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:      noarch

%description
Since long ago, I wanted to make a comic X11 mouse theme, funny and
entertaining. Also always had in my mind to do with ownership of
multi sizes. Although some people find it difficult topics in the
installation of multi sizes, but there is always the solution to
offer them as a package in various sizes.

%prep
%setup -q -n %{theme_name}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}
cp -a * $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root,-)
%{_datadir}/icons/%{theme_name}

%changelog
* Thu Jan 02 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 0.11
- Rebuilt for Fedora
