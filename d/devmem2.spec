Name:           devmem2
Version:        1.0
Release:        17.43
Summary:        Simple program to read/write from/to any location in memory
License:        GPL-2.0+
Group:          Hardware/Other
URL:            https://free-electrons.com/pub/mirror/devmem2.c
Source:         devmem2-1.0.tar.gz
Patch1:         fix_usage_on_64_bits.patch

%description
Simple program to read/write from/to any location in memory.
Usage examples:
devmem2 0x48004B48 w 0x2 - write value 0x2 to addr 0x48004B48
devmem2 0x50000014 - read value from addr 0x50000014

%prep
%setup -q
%patch 1

%build
cc %{optflags} devmem2.c -o devmem2

%install
install -D -m 0755 devmem2 %{buildroot}%{_sbindir}/devmem2

%files
%{_sbindir}/devmem2

%changelog
* Mon Apr 06 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuilt for Fedora
* Fri May  5 2017 guillaume@opensuse.org
- Add fix_usage_on_64_bits.patch to fix boo#1032032
  It updates the current devmem2.c file by the one provided by
  Russel King to fix usage on 64 bits systems.
* Fri Nov 13 2015 mpluskal@suse.com
- Use optflags
- Cleanup spec file with spec-cleaner
* Fri Mar  9 2012 guillaume.gardet@opensuse.org
- Initial release for devmem2 utility
