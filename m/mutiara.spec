Name: mutiara
Summary: Design motifs the fun way
Version: 0.14.0
Release: 1
Group: Amusements/Graphics
License: GPLv3
URL: https://mutiara.sourceforge.net/
Source0: https://sourceforge.net/projects/pasang-emas/files/pasang-emas/%{version}/%{name}-%{version}.tar.xz
BuildRequires: intltool
BuildRequires: gtk3-devel
BuildRequires: libgee06-devel
BuildRequires: gnome-doc-utils

%description
With Mutiara, you can easily create border motifs, such as the one that adorns
the border of this web page. Mutiara should also be of interest to fractal
collectors. There are plenty of interesting specimens waiting to be discovered.

%prep
%setup -q
#sed -i 's|3\.8\.4|3.8.2|' configure*

%build
%configure
make %{?_smp_mflags}

%install
%make_install
mv %{buildroot}%{_datadir}/%{name} %{buildroot}%{_datadir}/pixmaps

%files
%doc AUTHORS NEWS ChangeLog COPYING README
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png
%{_datadir}/help/C/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.*

%changelog
* Fri Aug 21 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 0.14.0
- Rebuilt for Fedora
