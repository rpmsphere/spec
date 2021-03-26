Name:           clicfs
Version:        1.4.4
Release:        73.1
License:        GPLv2
Summary:        Compressed Loop Image Container
Group:          System/Filesystems
Source:         clicfs.tar.gz
BuildRequires:  cmake
BuildRequires:  e2fsprogs-devel
BuildRequires:  fuse-devel
BuildRequires:  gcc-c++
BuildRequires:  openssl-devel
BuildRequires:  xz-devel
Requires:       fuse

%description
Clic FS is a FUSE file system to mount a Compressed Loop Image
Container. It has several features that make it a good choice for live
systems. It will compress a Loop Image and export it as read write,
creating a copy on write behaviour.

%prep
%setup -c %{name}

%build
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} \
      -DLIB=%{_lib} \
      -DCMAKE_VERBOSE_MAKEFILE=TRUE \
      -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_SKIP_RPATH=1 .

%install
rm -rf "$RPM_BUILD_ROOT"
make DESTDIR=$RPM_BUILD_ROOT install

%files
%doc LICENCE
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Tue Oct 25 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4.4
- Rebuild for Fedora
* Mon Oct 17 2011 coolo@suse.com
- update to 1.4.4
  - provide clicfs_fsck to check if the cow file was
    written consistently
* Wed Sep  7 2011 coolo@suse.com
- update to 1.4.3
  - kill -USR1 detaches all open files for shutdown
* Wed Sep  7 2011 coolo@suse.com
- spec-cleaner
* Mon Aug 29 2011 coolo@novell.com
- update to 1.4.2
  - fix build with newer ld
* Wed Mar 23 2011 coolo@novell.com
- update to 1.4.1
  - upstream patch
  - support old fuse versions
* Mon Mar 21 2011 dmueller@suse.de
- fix crash when outfile is no longer writeable
* Mon Mar 21 2011 coolo@novell.com
- update to 1.4.0
  - rework COW file format (packed file format unchanged)
  - make use of more threads again
  - make COW syncing much more robust and faster too
* Tue Nov 30 2010 coolo@novell.com
- update to 1.3.10
  - still call pthread_join to catch the cow writing
* Mon Nov 29 2010 coolo@novell.com
- update to 1.3.9
  - call pthread_cancel when the thread is done
* Wed Nov 24 2010 coolo@novell.com
- update to 1.3.8
  - fix deadlock in writing cow files
* Wed Aug 25 2010 coolo@novell.com
- update to 1.3.7
  - make it more robust against read errors (bnc#629543)
* Tue Oct 13 2009 coolo@novell.com
- update to 1.3.6
  - sync cow file every second for now (bnc#544150)
* Thu Aug 27 2009 coolo@novell.com
- update to 1.3.5.1
  - fix stupid mistake with large parts
* Tue Aug 25 2009 coolo@novell.com
- update to 1.3.5
  - better defaults for little ram (bnc#533687)
* Tue Aug 18 2009 coolo@novell.com
- update to 1.3.4
  - better data structure for cache
  - limit cache to 100MB
* Wed Aug 12 2009 coolo@novell.com
- update to 1.3.3
  - fix crash without logger
  - fix endless loop on read errors
* Wed Aug 12 2009 coolo@novell.com
- update to 1.3.2
  - allocate less memory in mkclicfs
* Tue Aug 11 2009 coolo@novell.com
- update to 1.3.1
  - smaller bug fixes while testing live cd profiling
* Mon Aug 10 2009 coolo@novell.com
- update to 1.3
  - caching readonly is dynamic now and profiled data
    is stored in large parts
* Thu Aug  6 2009 coolo@novell.com
- update to 1.2:
  - implement cow on special devices use case
* Tue May 19 2009 coolo@novell.com
- use fseeko instead of fseek (bnc#504627)
* Mon May 18 2009 coolo@novell.com
- make the file size 64bit (bnc#504627)
* Mon May 18 2009 coolo@novell.com
- don't confuse num_pages with write_pages (bnc#504700)
* Mon May 11 2009 coolo@suse.de
- fix corruption when writing short blocks
* Tue May  5 2009 coolo@suse.de
- if the cow file is read only, then just read it
* Mon Apr 20 2009 coolo@suse.de
- fixing license
* Mon Apr 20 2009 coolo@suse.de
- catch more errors
* Fri Apr 17 2009 coolo@suse.de
- initial package
