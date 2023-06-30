%undefine _debugsource_packages

Name:           ftpcopy
Version:        0.6.7
Release:        8.1
License:        GPL-2.0
Summary:        FTP Mirroring Tool
URL:            https://www.ohse.de/uwe/ftpcopy.html
Group:          Productivity/Networking/Web/Utilities
Source:         https://www.ohse.de/uwe/ftpcopy/%{name}-%{version}.tar.gz

%description
ftpcopy is a small mirror-like utility to copy files or directory trees
with FTP. ftpcopy understands EPLF and traditional listing formats.

%prep
%setup -qn web

%build
cd %{name}-%{version}
export CFLAGS="%{optflags}"
make

%install
rm -rf $RPM_BUILD_ROOT
cd %{name}-%{version}
install -d 0755 $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install -m 0755 command/* $RPM_BUILD_ROOT/%{_bindir}/
install -pm 0644 doc/* $RPM_BUILD_ROOT%{_mandir}/man1/

%files
%{_bindir}/ftp*
%doc %{_mandir}/man?/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Aug 01 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6.7
- Rebuilt for Fedora
* Mon Nov  7 2011 lazy.kent@opensuse.org
- Corrected License tag.
- Use full URL as a source.
- man pages marked as doc.
- spec clean up.
* Tue Oct 13 2009 lazy.kent.suse@gmail.com
- spec-file corrected.
* Thu Apr 16 2009 lazy.kent.suse@gmail.com
- Initial package created - 0.6.7.
