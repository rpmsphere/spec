%undefine _debugsource_packages

Name:		udevil		
Version:	0.4.4
Release:	5.1
Summary:	Mount and unmount without password
Group:		System Environment/Daemons
License:	GPLv3+
URL:		http://ignorantguru.github.com/udevil/
Source0:	https://github.com/IgnorantGuru/%{name}/archive/%{name}-%{version}.tar.gz
BuildRequires:	intltool, gettext
BuildRequires:	systemd-devel, glib2-devel

%description
udevil is a command line Linux program which mounts and unmounts 
removable devices without a password, shows device info, and monitors 
device changes. It can also mount ISO files, nfs://, smb://, ftp://, 
ssh:// and WebDAV URLs, and tmpfs/ramfs filesystems

%prep
%setup -q
sed -i 's/-o root -g root -m 4755//g' src/Makefile.in
sed -i '20i #include <sys/stat.h>' src/device-info.h

%build
./configure --prefix=/usr --libdir=/usr/lib
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
%find_lang %{name}
mv %{buildroot}%{_unitdir}/devmon@.service %{buildroot}%{_unitdir}/devmon.service

%post
%systemd_post devmon.service

%preun
%systemd_preun devmon.service

%postun
%systemd_postun devmon.service

%files -f %{name}.lang
%doc AUTHORS COPYING README
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%config(noreplace) %{_sysconfdir}/conf.d/devmon
%attr(4755,-,-) %{_bindir}/%{name}
%{_bindir}/devmon
%{_unitdir}/devmon.service

%changelog
* Wed May 06 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.4
- Rebuilt for Fedora
* Wed Jan 08 2014 Simone Sclavi <darkhado@gmail.com> 0.4.3-1
- Initial build
