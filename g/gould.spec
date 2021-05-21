Name:           gould
Version:        1.2.2
Release:        1
License:        GPL
Source0:        %{name}-%{version}.tar.gz
Vendor:         Mauro DePalma
URL:            http://www.softcraft.org/projects/gould
Group:          Applications/Desktop
Summary:        A GTK2 ultra-light desktop environment
BuildRequires:  gtk2-devel, libxml2-devel
Obsoletes:	gsnapshot

%description
The goal of GOULD is to provide an ultra-light desktop environment.
* gpanel - configurable desktop panel with builtin shortcuts manager
* gdisplay - imager viewer with directory browser
* gsnapshot - screen, window and region capture
* grdesktop - rdesktop frontend

%prep
%setup -q
sed -i 's/ -lrpmdb/ /' src/system/Makefile*

%build
CFLAGS='-fPIC -I/usr/include/libxml2 -lX11 -lm -lXext -lgmodule-2.0' ./configure --prefix=/usr
%{__make}

%install
%{__make} DESTDIR=%{buildroot} install

%clean
%__rm -rf %{buildroot}

%files
%{_bindir}/*
%{_datadir}/*
%{_libdir}/lib*
%{_libdir}/pkgconfig/*
%{_includedir}/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2.2
- Rebuilt for Fedora
