Name:           littleutils
Version:        1.2.5
Release:        1
License:        GPL-3.0
Summary:        Collection of Small and Simple Utilities
URL:            https://sourceforge.net/projects/littleutils/
Group:          Productivity/File utilities
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz
BuildRequires:  libjpeg
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  p7zip
BuildRequires:  pngcrush
BuildRequires:  gifsicle
BuildRequires:  xz

%description
File utilities:
filedate, filehash, filemode, filenode, fileown, randomize, lrealpath,
tempname

Image processing utilities:
imagsize, jpgcom, pngrecolor, pngstrip

Text file "cleanup" utilities:
notabs, notrail, lreplace

Compression optimization utilities:
opt-gif, opt-jpg, opt-png, recomp-jpg, to-7zip, to-bzip, to-gzip,
to-lzma, to-xz

File maintenance utilities:
lowercase, uppercase, frenum, pren, repeats, wipe-free

%prep
%setup -q

%build
export CFLAGS="%{optflags}"
./configure --prefix=%{_prefix}
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT%{_prefix} install
make prefix=$RPM_BUILD_ROOT%{_prefix} install-extra
# filesize is provided by aaa_base.
rm -f $RPM_BUILD_ROOT%{_bindir}/filesize,%{_mandir}/man1/filesize.1}
cd $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc BUGS ChangeLog FAQ LICENSES NEWS README TODO
%{_bindir}/*
%{_libdir}/%{name}
%doc %{_mandir}/man?/*

%changelog
* Sun Oct 16 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2.5
- Rebuilt for Fedora
* Mon Jun 18 2012 lazy.kent@opensuse.org
- Update to 1.0.26.
  * Added nanosecond timestamp support to filedate for systems and
    output formats that support it.
  * Made filenode compatible with 64-bit inode numbers.
  * Updated the FAQ and several manpages to better explain how the
    littleutils compare to coreutils.
* Tue Jan 17 2012 lazy.kent@opensuse.org
- Update to 1.0.25.
  * Added to-gzip utility.
  * Add capability to handle .lzo (lzop) files.
  * Improved use of file utility output, and updated manpages.
  * "realpath" renamed to "lrealpath".
* Tue Nov  8 2011 lazy.kent@opensuse.org
- Corrected License tag.
- Use full URL as a source.
- rpm changelog improved.
- spec clean up.
* Sun Mar  6 2011 lazy.kent@opensuse.org
- Update to 1.0.24.
  * Added new littleutil wipe-free, which overwrites all free space
    in a filesystem with zeros.
  * Added -a option to opt-jpg and recomp-jpg to control whether or
    not trials with arithmetic encoding will be allowed.
  * Updated lreplace, notabs, and notrail to print a comment when
    a file is modified.
  * The filehash utility now uses about 2%% less CPU time, which in
    turn means that the repeats utility now uses about 2%% less CPU
    time.
  * Added notes to several manpages that describe how to take
    advantage of parallel processing.
- Removed filesize (conflicts with aaa_base).
- Marked man pages as docs.
* Wed Jul 21 2010 lazy.kent.suse@gmail.com
- spec-file cleanup
* Sat Nov  7 2009 lazy.kent.suse@gmail.com
- Update to 1.0.23.
- Removed unneeded patches.
- Back 7zip support.
* Mon Nov  2 2009 lazy.kent.suse@gmail.com
- Update to 1.0.22.
  * Added new littleutil fileown, which allows a query of a file's
    uid/username or gid/group name.
  * Added -m option to opt-jpg to control whether comments and
    other extra markers are copied with the JPEG files.
- Splitted changelog.
* Thu Oct 15 2009 lazy.kent.suse@gmail.com
- Removed 7zip support.
- Corrected Summary.
* Wed Jul 22 2009 lazy.kent.suse@gmail.com
- Description corrected.
* Sat Jul 18 2009 lazy.kent.suse@gmail.com
- libexec moved to lib or to lib64.
* Wed Jun 24 2009 lazy.kent.suse@gmail.com
- Initial package created - 1.0.21.
