Name:           gsnapshot
Version:        1.1
Release:        1
License:        GPL
Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}-%{version}-language.c
Source2:        %{name}.desktop
Source3:        %{name}.png
Vendor:         Mauro DePalma
URL:            https://www.softcraft.org/gsnapshot/
Group:          Applications/Multimedia
Summary:        A GTK2 application for capturing a screen snapshot
BuildRequires:  gtk2-devel, libxml2-devel, libwnck-devel, libX11-devel, libXmu-devel

%description
A GTK2 application for capturing a screen snapshot of the entire screen,
a window or a region, with a simple user interface.

%prep

%setup -q
%__cp -f %{SOURCE1} src/common/language.c
sed -i -e 's|-lwnck|-lwnck-1|' -e 's|LIBS = |LIBS = -lX11 -lm -lgmodule-2.0 |' -e 's|-D__USE_GNU|-D__USE_GNU -fPIC -I/usr/include/libxml2|' src/*/Makefile.am

%build
export CFLAGS=${CFLAGS/-Werror=format-security/}
./autogen.sh
./configure --prefix=/usr
%{__make}

%install
%{__make} DESTDIR=%{buildroot} install
%{__install} -D -m 644 %{SOURCE3} %{buildroot}%{_datadir}/pixmaps/%{name}.png
%{__install} -D -m 644 %{SOURCE2} %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%{_bindir}/%{name}
%exclude %{_bindir}/gcontrol
%exclude %{_bindir}/gdisplay
%exclude %{_bindir}/gpanel
%exclude %{_datadir}/panel  
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%exclude %{_libdir}/*
%exclude /usr/lib/*
%exclude %{_includedir}/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1
- Rebuilt for Fedora
