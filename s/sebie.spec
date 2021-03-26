Summary: Semi Batched Image Editor
Name: sebie
Version: 0.9.2
Release: 4.1
License: GPLv2
Group: Graphics
Source: http://www.ciselant.de/projects/sebie/%{name}-%{version}.tar.gz
URL: http://www.ciselant.de/projects/sebie/
BuildRoot: %{_tmppath}/%name-buildroot
BuildRequires: gtk2-devel
BuildRequires: glib2-devel

%description
SeBIE stands for Semi-Batched-Image-Editor.

%prep
%setup -q

%build
./configure --prefix=/usr
make

%install
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/%{name}

%changelog
* Sun Sep 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.2
- Rebuild for Fedora
