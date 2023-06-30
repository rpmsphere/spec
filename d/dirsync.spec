%undefine _debugsource_packages

Summary: Tool to synchronize directories
Name: dirsync
Version: 1.11
Release: 5.1
License: GPL
Group: Applications/System
URL: https://www.viara.cn/en/dirsync.htm
Source: https://www.viara.cn/download/dirsync-1_11.tar.gz

%description
dirsync is a directory synchronizer that takes a source and destination
directory as arguments and recursively ensures that the two directories
are identical. It can be used to create incremental copies of large chunks
of data.

%prep
%setup -q -c
rm %{name} %{name}.exe

%build
%{__make} %{?_smp_mflags} linux

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 dirsync %{buildroot}%{_bindir}/dirsync
%{__install} -Dp -m0644 dirsync.1 %{buildroot}%{_mandir}/man1/dirsync.1

%clean
%{__rm} -rf %{buildroot}

%files
%doc readme.txt
%doc %{_mandir}/man1/dirsync.1*
%{_bindir}/dirsync

%changelog
* Sun Jun 16 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.11
- Rebuilt for Fedora
* Tue Nov 04 2008 Dag Wieers <dag@wieers.com> -  - 7981/dag
- Initial package. (using DAR)
