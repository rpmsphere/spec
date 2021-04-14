Name:		fqterm		
Version:	0.9.8.4
Release:	7.1
Summary:	BBS client designed for BBS browsing	
Group:		Applications/Internet
License:	GPLv2+
URL:		http://code.google.com/p/fqterm/
Source0:	https://codeload.github.com/mytbk/fqterm/tar.gz/0.9.8.4#/%{name}-%{version}.tar.gz
BuildRequires:	qt4-devel
BuildRequires:	openssl-devel
BuildRequires:	python2-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	cmake
BuildRequires:	desktop-file-utils

%description
FQTerm is one of the most widely used BBS client in China, it supports
telnet/ssh1/ssh2 protocols and can process ANSI control sequences. It
can be used to login BBS sites or *NIX hosts.

Almost all the BBSes in Greater China Region are in BIG5 or GBK encoding.
So FQTerm only support these two encodings and ASCII.

%prep
%setup -q
sed -i 's/\r//g' README.txt
sed -i 's/\r//g' doc/*.txt
sed -i 's/\r//g' res/credits
#sed -i 's|siteManager(this, false)|siteManager(this, 0)|' src/fqterm/fqterm_frame.cpp

%build
export CXXFLAGS="-fPIC -Wno-narrowing"
export PATH=%{_qt4_bindir}:$PATH
# enable BUILD_SHARED_LIBS will generate some shlibs that cannot be installed
# by simply type 'make install'
%cmake -DBUILD_SHARED_LIBS:BOOL=OFF 
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

rm -rf %{buildroot}%{_datadir}/FQTerm/dict/*.ts
rm -rf %{buildroot}%{_datadir}/FQTerm/fqterm.sh

sed -i -e '/^Icon.*$/c Icon=fqterm' %{buildroot}%{_datadir}/applications/fqterm.desktop
desktop-file-install --vendor "" \
	--dir %{buildroot}%{_datadir}/applications \
	--remove-category Application \
	--add-category RemoteAccess \
	%{buildroot}%{_datadir}/applications/fqterm.desktop

%clean
rm -rf %{buildroot}

%files
%doc README.txt LICENSE doc/*
%{_bindir}/%{name}*
%{_datadir}/FQTerm
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png

%changelog
* Tue Aug 15 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.8.4
- Rebuilt for Fedora
* Thu Apr 29 2010 Chen Lei <supercyper@163.com> - 0.9.6.8-1
- Update to 0.9.6.3
- Add qt runtime dependency
- Fix some rpmlint warings
* Tue Nov 24 2009 Chen Lei <supercyper@163.com> - 0.9.6.3-1
- Update to 0.9.6.3
* Sun Nov 22 2009 Chen Lei <supercyper@163.com> - 0.9.5.2-2
- Clean up the spec file
* Sun Nov 22 2009 Chen Lei <supercyper@163.com> - 0.9.5.2-1
- Fix the spec file
* Sat Nov 21 2009 Chen Lei <supercyper@163.com> - 0.9.5.2-0
- Initial rpm build
