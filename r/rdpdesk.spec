Name:           rdpdesk
Version:        3.2
Release:        19.1
License:        GPLv2
Summary:        Remote Desktop (RD) management solution
URL:            http://sourceforge.net/projects/rdpdesk/
Group:          Productivity/Networking/Diagnostic
Source:         http://sourceforge.net/projects/rdpdesk/files/Releases/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  imake
BuildRequires:  libXt-devel
BuildRequires:  libXaw-devel
BuildRequires:  libjpeg-devel
BuildRequires:  wxGTK-devel
BuildRequires: compat-openssl10-devel

%description
RD Connection Manager is a Remote Desktop (RD) management solution for
administrating remote computers and servers. It's a graphical frontend
for remote desktop tools. Supports RDP, ICA and VNC.

%prep
%setup -q
sed -i '/gspawn\.h/d' src/proto/*Connection_nix.hpp
sed -i '/wxHandleFatalExceptions/d' src/main.cpp
%ifarch %ix86
sed -i 's|return NULL|return 0L|' src/gui/tree_group.cpp
%endif

%build
export LDFLAGS+=" -lgobject-2.0 -lX11 -lgdk-x11-2.0 -lgtk-x11-2.0 -lcrypto"
%configure --disable-static
make

%install
%make_install

%clean
%{__rm} -rf %{buildroot}

%files
%{_bindir}/%{name}*
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo
%{_datadir}/pixmaps/%{name}.png

%changelog
* Mon Oct 21 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 3.2
- Rebuilt for Fedora
