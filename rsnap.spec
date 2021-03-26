Name: rsnap
Summary: Backup and snapshot utility
Version: 0.6
Release: 3.1
Group: Productivity/Archiving/Backup
License: GPL
Source: %{name}-%{version}.tar.gz
URL: http://web.chad.org/projects/rsnap/
BuildRoot: %{_tmppath}/%{name}-%{version}-build
BuildArch: noarch

%description
rsnap is a backup and snapshot utility based on rsync. rsnap will not only save
the state of your files of the last backup, but it will also retain previous
states - as many as you like. This is done in an efficient way, so that only
files that have changed will occupy additional space. Even better, as rsnap is
a thin wrapper around rsync which adds snapshot rotating and creation, the
changes you need to make to your existing backup script are minimal.

%prep

%setup

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
install -m 755 %{name} $RPM_BUILD_ROOT/%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc LICENSE
%{_bindir}/%{name}

%changelog
* Sun Sep 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6
- Rebuild for Fedora
* Tue Feb 24 2009 Lenz Grimmer <lenz@grimmer.com>
 - Update to version 0.6
* Fri Jul 18 2008 Lenz Grimmer <lenz@grimmer.com>
 - Initial version (0.01)
