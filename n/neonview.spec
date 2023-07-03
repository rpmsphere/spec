%undefine _debugsource_packages

Name:          neonview
Version:       0.8.2
Release:       5.1
Summary:       A simple, minimalist and lightweight image viewer for the Linux platform
Group:         Graphics
License:       GPLv2+
URL:           https://www.tuxarena.com/intro/neonview.php
Source0:       https://www.tuxarena.com/intro/files/%{name}-%{version}-src.tar.gz
Patch0:        strip-remove.patch
BuildRequires: pkgconfig(gtk+-x11-3.0)

%description
NeonView is a simple, minimalist and lightweight image viewer
for the Linux platform, written in C and GTK, 
completely free and open-source. The goal of NeonView is 
to stay lightweight while also providing ease of use 
and only the necessary features a basic image viewer should have.
NeonView supports a bunch of image formats, and it will remember
settings like fit to window images between sessions or lock fit 
to window for the current session. Basic manipulation functions
like zooming or rotating are also available.

%prep
%setup -q -n %{name}-%{version}-src
%patch0 -p1

%build
make

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 %{name} %{buildroot}%{_bindir}/

%files
%doc COPYING ChangeLog *.txt *.html
%{_bindir}/neonview

%changelog
* Wed Jul 08 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8.2
- Rebuilt for Fedora
* Fri Jul 25 2014 Denis Silakov <denis.silakov@rosalab.ru> 0.8.2-2
+ Revision: 17e2aaa
- MassBuild#464: Increase release tag
