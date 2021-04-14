%undefine _debugsource_packages

Name:           qwit
Version:        1.1pre2
Release:        12.1
URL:            http://code.google.com/p/qwit/
License:        GPLv3
Group:          Network/Instant messaging
Summary:        Qt4 cross-platform client for Twitter
Source:         http://qwit.googlecode.com/files/qwit-1.1-pre2-src.tar.bz2
Source1:        qwit.desktop
Source2:        qwit-tango-icons.tar.gz
Patch:          qwit-1.0-r303-no-shortner-option.diff
BuildRequires:  gcc-c++ qt4-devel intltool qoauth-devel
BuildRequires:  qca-devel

%description
Qt4 cross-platform client for Twitter. Also contains a minor modification
to allow users to disable URL shortening.

%package devel
Requires:       %{name} = %{version}
Requires:       qt4-devel
Summary:        Qt4 cross-platform client for Twitter (Development libraries)
Group:          Development/Libraries/C and C++

%description devel
Qt4 cross-platform client for Twitter (Development libraries).

%prep
%setup -q -n qwit-1.1-pre2-src -a 2
%patch -p1

%build
qmake-qt4 PREFIX=/usr 
make %{?jobs:-j%jobs}

%install
%__install -D -m755 %{name} %{buildroot}%{_bindir}/%{name}
%__install -D -m644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop
%__install -D -m644 images/%{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc COPYING README
%{_bindir}/%{name}  
%{_datadir}/applications/%{name}.desktop  
%{_datadir}/pixmaps/%{name}.png 

%changelog
* Sun Mar 10 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1pre2
- Rebuilt for Fedora
* Sun Apr 11 2010 IBBoard
- Updated to r323 (changes at http://code.google.com/p/qwit/source/list)
* Mon Dec 21 2009 IBBoard
- Updated to r303 (stops pop-up when showing more messages)
- Replaced icons with nicer and properly sized Tango icons
* Sat Nov 28 2009 IBBoard
- Initial build
- Added small patch to re-instate "no shortner" option
