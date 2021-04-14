Name:			urlencode
Version:		1.0.3
Release:		2.1
License:		GPLv2
Group:			Productivity/Networking/Web/Utilities
Source:			%{name}-%{version}.tar.bz2
URL:			http://www.davjam.org/~davjam/linux/urlencode/
Summary:		Converts a text string to HTML encoding
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Converts a text string to a HTML entity encoded string.

%prep
%setup -q -n %{name}
./bootstrap.sh

%build
%configure
%{__make} CFLAGS="%{optflags}" %{?jobs:-j%jobs}

%install
rm -rf $RPM_BUILD_ROOT
install -D -m755 %{name} $RPM_BUILD_ROOT/%{_bindir}/%{name}

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README VERSION

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sun Aug 05 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.3
- Rebuilt for Fedora
* Tue Apr 13 2004 David Bolt <urlencode@davjam.org> 1.0.1
- Minor bug-fix
* Mon Apr 12 2004 David Bolt <urlencode@davjam.org> 1.0.0
- Initial release
