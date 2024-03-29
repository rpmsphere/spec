%undefine _debugsource_packages

Name:           myrescue
Version:        0.9.8
Release:        1
Summary:        Rescue the still-readable data from a damaged harddisk
License:        GPL-2.0+
Group:          Productivity/File utilities
URL:            https://myrescue.sourceforge.net/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

%description
myrescue is a program to rescue the still-readable data from a
damaged harddisk. It is similar in purpose to dd_rescue, but it
tries to quickly get out of damaged areas to first handle the not
yet damaged part of the disk and return later.

%prep
%setup -q -c

%build
sed -i 's|-Wall|-Wall -fPIE|' src/Makefile
make %{?_smp_mflags} -C src

%install
install -Dpm 0755 src/myrescue %{buildroot}%{_bindir}/myrescue
install -Dpm 0644 doc/myrescue.1 %{buildroot}%{_mandir}/man1/myrescue.1
gzip -9f %{buildroot}%{_mandir}/man1/myrescue.1
install -Dpm 0644 doc/myrescue.de.1 %{buildroot}%{_mandir}/de/man1/myrescue.1
gzip -9f %{buildroot}%{_mandir}/de/man1/myrescue.1

%files
%doc AUTHORS COPYING ChangeLog README TODO
%{_bindir}/myrescue
%doc %{_mandir}/man1/myrescue.1.*
%doc %{_mandir}/de/man1/myrescue.1.*

%changelog
* Sun Oct 16 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.8
- Rebuilt for Fedora
* Sun Aug 26 2012 asterios.dramis@gmail.com
- Removed %%clean section (not needed anymore).
* Sun Oct 30 2011 asterios.dramis@gmail.com
- Initial release (version 0.9.4).
- Added a patch (Makefile_fix.patch) to make the package use CFLAGS from spec
  file.
