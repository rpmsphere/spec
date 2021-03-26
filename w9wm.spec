Name: w9wm
Summary: 9wm based window manager
Version: 0.4.2
Release: 3.1
Group: Converted/x11
License: see /usr/share/doc/w9wm/copyright
URL: http://www.drieu.org/code/w9wm.en.html
Source0: http://www.drieu.org/code/w9wm/src/w9wm-%{version}.tar.gz
BuildRequires: libXext-devel
BuildRequires: libX11-devel

%description
w9wm is a quick and dirty hack based on 9wm. It provides support for
virtual screens as well as for keyboard bindings.

%prep
%setup -q -n %{name}-%{version}.orig
mv Makefile.no-imake Makefile

%build
make %{?_smp_mflags}

%install
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dm644 %{name}.man %{buildroot}%{_mandir}/man1/%{name}.1

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

%changelog
* Fri Mar 31 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.2
- Rebuild for Fedora
