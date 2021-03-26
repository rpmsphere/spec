Name:          acpi4asus
Version:       0.41
Release:       3.1
Summary:       Allow owners of Asus laptops to use all the functionalities
Group:         System/Kernel and Hardware
URL:           http://sourceforge.net/projects/acpi4asus/
Source:        http://downloads.sourceforge.net/acpi4asus/acpi4asus-%{version}.tar.bz2
License:       GPL
BuildRoot:     %{_tmppath}/%{name}-%{version}-root

%description
This project is a linux driver that allow owners of Asus laptops to use all the 
functionalities of their computer such as special keys, special LEDs, control 
of brightness, ...
This project will eventually be merged in the acpi linux code.

%prep
%setup -q

%build
# build only the daemon, the kernel module is already in the linux kernel
sed -i "s|/usr/local/|/usr/|" asus_acpid/Makefile

make -C asus_acpid

%install
rm -rf $RPM_BUILD_ROOT
make -C asus_acpid install \
   INSTALLDIR=$RPM_BUILD_ROOT \
   INSTPREFIX=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}-%{version}
cp Changelog LICENSE README \
   $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}-%{version}
cp -R samples \
   $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/asus_acpid
%dir %{_defaultdocdir}/%{name}-%{version}
%{_defaultdocdir}/%{name}-%{version}/*
%{_mandir}/man8/* 

%changelog
* Wed Jun 29 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.41
- Rebuild for Fedora

* Sun Jun 17 2007 Tiziana Ferro <tiziana.ferro@email.it> 0.41-1mamba
- update to 0.41

* Tue Apr 06 2004 Davide Madrisan <davide.madrisan@qilinux.it> 0.27-1qilnx
- new version rebuild
- added documentation and example scripts

* Thu Jul 10 2003 Silvan Calarco <silvan.calarco@qinet.it> 0.24a-1qilnx
- first build for acpi4asus
