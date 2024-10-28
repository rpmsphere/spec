Name:                   clone2fs
Version:                1.3.0
Release:                7.1
Summary:                Clone ext2/ext3 File Systems
Source:                 https://www.mr511.de/software/clone2fs-%{version}.tar.gz
Patch1:                 clone2fs-makefile.patch
URL:                    https://www.mr511.de/software/
Group:                  Productivity/File utilities
License:                GNU General Public License version 2 (GPL v2)
BuildRequires:  e2fsprogs-devel
BuildRequires:  gcc make glibc-devel

%description
clone2fs is an utility to clone an ext2/ext3 filesystem.

Unlike dd, clone2fs does not copy the whole volume but only blocks that are
actually in use. Therefore, it is usually faster. It's also faster than
dump/restore, tar or similar backup software because it accesses the source
and destination volumes sequentially most of the time.

Note that clone2fs allows you to clone a mounted file system without warning,
even if it's writable. In the latter case, you have to run e2fsck on the
resulting image in order to make it consistent. Since copying takes a while,
changes made while clone2fs is working may or may not appear in the clone. If
you need an exact clone, umount the source file system, or remount it in
read-only mode.

Authors:
--------
    Michael Riepe

%prep
%setup -q
%patch 1

%build
%__make %{?jobs:-j%{jobs}} \
                  CC="%__cc" \
                  OPTFLAGS="%{optflags}"

%install
%__rm -rf "$RPM_BUILD_ROOT"
make DESTDIR=$RPM_BUILD_ROOT install
h=/usr/share/doc/licenses/md5/$(md5sum COPYING|cut -f1 -d" ")
test -e "$h" && %__ln_s -f "$h" .

%files
%doc COPYING NEWS README
/sbin/clone2fs

%changelog
* Wed Nov 30 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3.0
- Rebuilt for Fedora
* Mon Feb 01 2010 Pascal Bleser <pascal.bleser@opensuse.org> 1.3.0
- update to 1.3.0:
  * fixes a bug that caused invalid images to be written when
    the -s option was used and the destination was a file
    rather than a pipe
* Sat Aug 23 2008 Pascal Bleser <guru@unixtech.be> 1.2.0
- new package
