Name:           lorder
Version:        6.1.10
Release:        3.1
Summary:        List Dependencies for Object Files
Source:         https://ftp.de.debian.org/debian/pool/main/b/bsdmainutils/bsdmainutils_%{version}.tar.bz2
Group:          Development/Languages/C and C++
License:        BSD License
BuildRequires:  make
BuildArch:     noarch
Requires:      binutils
Requires:      /usr/bin/awk
Requires:      /usr/bin/sort
Requires:      /usr/bin/join
Requires:      /bin/grep

%description
The lorder utility uses nm(1) to determine interdependencies in the list of
object files specified on the command line. Lorder outputs a list of file
names where the first file contains a symbol which is defined by the second
file.

The output is normally used with tsort(1) when a library is created to
determine the optimum ordering of the object modules so that all references
may be resolved in a single pass of the loader.

%prep
%setup -q -n "bsdmainutils-%{version}"

%build
%__make -C usr.bin/lorder lorder

%install
%__install -D -m0755 usr.bin/lorder/lorder "$RPM_BUILD_ROOT%{_bindir}/lorder"
%__install -D -m0644 usr.bin/lorder/lorder.1 "$RPM_BUILD_ROOT%{_mandir}/man1/lorder.1"

%files
%doc README
%{_bindir}/lorder
%doc %{_mandir}/man1/lorder.1*

%changelog
* Sun Oct 28 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 6.1.10
- Rebuilt for Fedora
* Tue Jun  2 2009 Pascal Bleser <pascal.bleser@opensuse.org> 6.1.10
- new package
