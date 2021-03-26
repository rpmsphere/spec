Name:          eciadsl
Version:       0.12
Release:       2.1
Summary:       User space tools for ECI HiFocus USB modem or Globespan based modem
Group:         System/Kernel and Hardware
URL:           http://eciadsl.flashtux.org
Source:        http://eciadsl.flashtux.org/download/eciadsl-usermode-%{version}.tar.gz
Source1:       http://eciadsl.flashtux.org/download/eciadsl-synch_bin.tar.bz2
Patch0:        %{name}-usermode-0.12-kernel_include.patch
License:       GPL
Obsoletes:     eciadsl-usermode
Provides:      eciadsl-usermode

%description
With this driver you can connect your computer to the Internet under Linux,
using ECI HiFocus USB modem or Globespan based modem.

%prep
%setup -q -n eciadsl-usermode-%{version} -a1
%patch0 -p1

%build
%configure
make CFLAGS+="-Wno-format-security -std=gnu89"

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
#mkdir -p $RPM_BUILD_ROOT
#make install ROOT=$RPM_BUILD_ROOT
install eciadsl-synch_bin/*.bin eciadsl-synch_bin/README* $RPM_BUILD_ROOT/etc/eciadsl/

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/eciadsl.desktop << EOF
[Desktop Entry]
Name=ECI ASDL USB Modem configuration 
Comment=ECI Linux driver configuration for USB modems
Comment[it]=Configurazione del driver ECI per modem ADSL USB
Exec=eciadsl-config-tk
Type=Application
Terminal=0
Icon=gnome-ppp
Categories=Application;Network;
X-KDE-RootOnly=true
X-KDE-SubstituteUID=true
X-KDE-Username=root
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%dir %{_sysconfdir}/eciadsl
%{_sysconfdir}/eciadsl/*
%{_bindir}/*
%doc README TROUBLESHOOTING NEWS COPYING
%{_datadir}/applications/eciadsl.desktop

%changelog
* Wed Jun 29 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.12
- Rebuild for Fedora
* Sun May 03 2009 Silvan Calarco <silvan.calarco@mambasoft.it> 0.12-2mamba
- fixed desktop menu entry to launch eciadsl-config-tk
- added synch_bin package
* Sat Sep 29 2007 Silvan Calarco <silvan.calarco@mambasoft.it> 0.12-1mamba
- update to 0.12
* Mon Jun 28 2004 Silvan Calarco <silvan.calarco@qilinux.it> 0.9-2qilnx
- kde menu link added
* Mon Jun 28 2004 Silvan Calarco <silvan.calarco@qilinux.it> 0.9-1qilnx
- first build
