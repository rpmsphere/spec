Name:           mhddfs
Summary:        Fuse-based file system for unifying several mount points into one
Version:        0.1.39
Release:        6
License:        GPLv3+
URL:            https://mhddfs.uvw.ru/
Source:         https://mhddfs.uvw.ru/downloads/%{name}_%{version}.tar.gz

#Make sure it builds with system CFLAGS
Patch0:         mhddfs-cflags.patch

BuildRequires:  fuse-devel libattr-devel uthash-devel
Requires:       fuse%{?_isa}

%description
This FUSE-based file system allows mount points (or directories) to be combined,
simulating a single big volume which can merge several hard drives or remote
file systems.  It is like unionfs, but can choose the drive with the most free
space to create new files on, and can move data transparently between drives.

%prep
%setup -q
%patch 0 -p1

%build
CFLAGS="$RPM_OPT_FLAGS -Wno-format-security" \
make %{?_smp_mflags}

%install
install -d $RPM_BUILD_ROOT/%{_bindir}
install -d $RPM_BUILD_ROOT/%{_mandir}/man1
install -m755 %{name} $RPM_BUILD_ROOT/%{_bindir}/%{name}
install -m644 %{name}.1 $RPM_BUILD_ROOT/%{_mandir}/man1/%{name}.1

%files
%doc README README.ru.UTF-8 LICENSE ChangeLog COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Sun Sep 05 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.39
- Rebuilt for Fedora
* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.39-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild
* Thu Jul 02 2015 Ralf Corsépius <corsepiu@fedoraproject.org> -  0.1.39-5
- BR: uthash-devel instead of uthash (Fix FTBFS).
* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.39-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild
* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.39-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild
* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.39-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild
* Sun May 18 2014 Filipe Rosset <rosset.filipe@gmail.com> - 0.1.39-1
- Rebuilt for new upstream version, spec cleanup, fixes rhbz #832823 
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.38-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.38-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild
* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.38-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild
* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.38-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild
* Mon Aug 15 2011 Jameson Pugh <imntreal@gmail.com> - 0.1.38-9
- Add RPM_OPT_FLAGS proper
* Wed Aug 10 2011 Jameson Pugh <imntreal@gmail.com> - 0.1.38-8
- Added RPM_OPT_FLAGS to CFLAGS
* Tue Aug 9 2011 Jameson Pugh <imntreal@gmail.com> - 0.1.38-7
- Left out build flags
* Thu Aug 4 2011 Jameson Pugh <imntreal@gmail.com> - 0.1.38-6
- Removed Group tag
* Thu Aug 4 2011 Jameson Pugh <imntreal@gmail.com> - 0.1.38-5
- Corrected Requires line
* Thu Aug 4 2011 Jameson Pugh <imntreal@gmail.com> - 0.1.38-4
- Made install locations more specific
* Thu Aug 4 2011 Jameson Pugh <imntreal@gmail.com> - 0.1.38-3
- Cleaned up SPEC
* Wed Aug 3 2011 Jameson Pugh <imntreal@gmail.com> - 0.1.38-2
- Added libattr-devel as a build requirement
* Tue Aug 2 2011 Jameson Pugh <imntreal@gmail.com> - 0.1.38-1
- Initial release
