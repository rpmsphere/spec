Name:                            cdu
Version:                         0.37
Release:                         6.1
Summary:                         Coloured Disk Usage
Source:                  https://arsunik.free.fr/pkg/cdu-%{version}.tar.gz
Patch1:                  cdu-mandir.patch
URL:                             https://arsunik.free.fr/prog/cdu.html
Group:                   Productivity/File utilities
License:                         GNU General Public License version 2 or later (GPL v2 or later)
BuildRequires:   perl
BuildRequires: perl-podlators
BuildArch:               noarch
Requires:                /usr/bin/du

%description
cdu (for Color du) is a perl script which call du and display a pretty
histogram with optional colors which allow to imediatly see the directories
which take disk space.

With no arguments, cdu reports the disk space for all subdirectories of the
current directory.
With only one directory argument, cdu reports the disk space for all
subdirectories of the given directory.

Authors:
--------
    Stephane Levant <stephane.levant@gmail.com>

%prep
%setup -q
%patch 1

%build
%__make

%install
%__rm -rf "$RPM_BUILD_ROOT"
%__make DESTDIR="$RPM_BUILD_ROOT%{_prefix}" install
%__chmod 0644 "$RPM_BUILD_ROOT%{_mandir}"/man*/*.*
h=/usr/share/doc/licenses/md5/$(md5sum COPYING|cut -f1 -d" ")
test -e "$h" && %__ln_s -f "$h" .

%files
%doc COPYING README
%{_bindir}/cdu
%doc %{_mandir}/man1/cdu.1.*

%changelog
* Wed Nov 30 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.37
- Rebuilt for Fedora
* Tue May 18 2010 pascal.bleser@opensuse.org
- update to 0.37:
  * an option was added for using high intensity colors
* Wed May  5 2010 pascal.bleser@opensuse.org
- update to 0.35:
  * an option was added to both print sizes in human readable
    format and sort directories by size
* Thu Feb 18 2010 pascal.bleser@opensuse.org
- update to 0.34:
  * an option was added to print sizes in human readable format
* Sun Feb 14 2010 pascal.bleser@opensuse.org
- new package (0.33)
