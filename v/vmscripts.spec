Name: vmscripts
Summary: Some helper scripts for VirtualBox & kvm virtual machines
Version: 1.3
Release: 12.1
License: GPL
Source: %{name}-%{version}.tar.bz2
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Group: Applications/Emulators
%define docdir %{_docdir}/%{name}-%{version}

%description
vboxlive: runs Linux live system in VirtualBox disk-less virtual machines
http://forums.opensuse.org/english/get-technical-help-here/how-faq-forums/unreviewed-how-faq/465445-running-linux-live-cds-disk-less-virtual-machines-under-virtualbox.html
VBoxExtensionPack: updates VirtualBox Extension pack: 
http://forums.opensuse.org/english/other-forums/development/programming-scripting/459800-update-virtualbox-4-0-extension-pack.html 
vm-bridge: converts virtual machines from NAT to bridge or bridge to NAT
http://forums.opensuse.org/english/other-forums/development/programming-scripting/453961-vm-bridge-convert-virtual-machines-nat-bridge-bridge-nat.html
vm-create: creates kvm virtual machines from anywhere to anywhere.
http://forums.opensuse.org/english/other-forums/development/programming-scripting/453962-vm-create-create-kvm-virtual-machines.html
popup library: displays dialogs in QT/GTK style (used by the other scripts)
http://forums.opensuse.org/english/other-forums/development/programming-scripting/452886-dialog-boxes-bash-scripts.html

Authors:  
--------
Agnelo de la Crotche (please_try_again) <agnelo@unixversal.com>

%prep
%setup -q

%build
# nothing to build

%install
install -d -m 0755 $RPM_BUILD_ROOT%{_bindir}
install -d -m 0755 $RPM_BUILD_ROOT%{_sysconfdir}
install -d -m 755 $RPM_BUILD_ROOT%{docdir}
install -m 0755 popup VBoxExtensionPack vboxlive vm-bridge vm-create $RPM_BUILD_ROOT%{_bindir}
install -m 0644 vm-create.cfg $RPM_BUILD_ROOT%{_sysconfdir}
install -m 0644 vboxlive.cfg $RPM_BUILD_ROOT%{_sysconfdir}

ln $RPM_BUILD_ROOT%{_bindir}/vm-bridge $RPM_BUILD_ROOT%{_bindir}/nat2bridge
ln $RPM_BUILD_ROOT%{_bindir}/vm-bridge $RPM_BUILD_ROOT%{_bindir}/bridge2nat

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING
%config (noreplace) %{_sysconfdir}/vm-create.cfg
%config (noreplace) %{_sysconfdir}/vboxlive.cfg
%{_bindir}/*

%changelog
* Wed Feb 01 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3
- Rebuilt for Fedora
* Mon Oct 17 2011 Agnelo de la Crotche <agnelo@unixversal.com> 1.3
- updated vboxlive to version 2.2
* Tue Oct 11 2011 Agnelo de la Crotche <agnelo@unixversal.com> 1.2
- updated vboxlive to version 2.1
- updated vm-create to version 2.5
* Thu Oct 6 2011 Agnelo de la Crotche <agnelo@unixversal.com> 1.1
- updated vboxlive to version 2.0
- fixewd minor bugs in popup and vm-create
* Thu Sep 20 2011 Agnelo de la Crotche <agnelo@unixversal.com> 1.0.1
- Fixed bug in vm listing on Mandriva and added function listvm
* Mon Sep 19 2011 Agnelo de la Crotche <agnelo@unixversal.com> 1.0
- initial build
