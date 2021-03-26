Name:           xremote
Version:        2.0
Release:        3.1
Summary:        A utility for grabbing a remote mouse and keyboard
Group:          User Interface/X Hardware Support
License:        GPLv2+
URL:            http://chakie.infa.fi/xremote/index.php3
Source0:        http://chakie.infa.fi/xremote/xremote-%{version}.tar.gz
Patch0:         xremote-2.0-gcc43.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  libX11-devel
BuildRequires:  libXtst-devel

%description
xremote is a small utility that allows you to grab the mouse and keyboard of
a remote display. Everything then done with the local mouse and keyboard is
mirrored by the remote display. Only useful as long as both displays can be
seen at the same time.

%prep
%setup -q
%patch0 -p1 -b .gcc43

%build
gcc $RPM_OPT_FLAGS -DVERSION="%{version}" -c xremote.cpp -o xremote.o
gcc -L%{_libdir} $(pkg-config --libs xtst x11) -lstdc++ xremote.o -o xremote

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -pm 0755 xremote $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -pm 0644 xremote.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc ChangeLog README
%{_bindir}/xremote
%{_mandir}/man1/xremote.*

%changelog
* Fri Oct 18 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0
- Rebuild for Fedora
* Tue Mar 18 2008 kwizart < kwizart at gmail.com > - 2.0-1
- Initial spec file
