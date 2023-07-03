%undefine _debugsource_packages
%global _default_patch_fuzz 2

Name:           popa3d
Version:        1.0.3
Release:        1
License:        BSD
BuildRequires:  gcc, coreutils, pam-devel, glibc-devel
Requires:       xinetd, shadow-utils
Group:          Networking/Mail
Summary:        Tiny POP3 daemon
URL:            https://www.openwall.com/popa3d/
Source0:        %name-%version.tar.gz
Source1:	popa3d-xinet
Source2:	popa3d-pam
Patch0:		popa3d-params.patch.bz2
Patch1:		popa3d-0.6.4.patch.bz2
Patch2:		popa3d-maildir.patch.bz2
Patch3:		popa3d-vname.patch.bz2

%description
popa3d is a tiny POP3 daemon designed with security as the primary goal.

%prep
%setup -q
%patch0 -p0 -b .popa3d-params
%patch1 -p0 -b .popa3d-log_ip
%patch2 -p0 -b .popa3d-maildir
%patch3 -p0 -b .popa3d-vname

%build
%{__make} LIBS="-lpam -lcrypt -Wl,--allow-multiple-definition"

%install
rm -rf "$RPM_BUILD_ROOT"
%__install -d $RPM_BUILD_ROOT%_var/empty
%__install -d $RPM_BUILD_ROOT%_sysconfdir/xinetd.d && \
%__install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%_sysconfdir/xinetd.d/popa3d
%__install -d $RPM_BUILD_ROOT%_sysconfdir/pam.d && \
%__install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%_sysconfdir/pam.d/popa3d
%makeinstall PREFIX=$RPM_BUILD_ROOT SBINDIR=$RPM_BUILD_ROOT%{_sbindir} MANDIR=$RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf "$RPM_BUILD_ROOT"

%pre
/usr/sbin/groupadd -r -f popa3d
/usr/sbin/useradd -r -g popa3d -d /dev/null -s /dev/null -n popa3d >/dev/null 2>&1 ||:

%postun
/usr/sbin/userdel popa3d

%files
%doc LICENSE INSTALL DESIGN CHANGES CONTACT VIRTUAL
%dir %_var/empty
%config(noreplace) %_sysconfdir/xinetd.d/popa3d
%config(noreplace) %_sysconfdir/pam.d/popa3d
%_mandir/man8/*
%_sbindir/*

%changelog
* Mon Oct 07 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.3
- Rebuilt for Fedora
* Tue May 13 2008 TI_Eugene <ti.eugene@gmail.com> 1.0.2
- Initial build for OBS
