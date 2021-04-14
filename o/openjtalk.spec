%undefine _debugsource_packages

Name: openjtalk
Version: 1.05
Release: 1
Summary: Japanese text-to-speech synthesis system
License: BSD
Group: System Environment/Libraries
URL: http://open-jtalk.sourceforge.net/
Source: open_jtalk-%{version}.tar.gz
BuildRequires: gcc-c++
BuildRequires: htsengine

%description
Open JTalk is a Japanese text-to-speech synthesis system.

%prep
%setup -q -n open_jtalk-%{version}
sed -i 's|std::make_pair<.*>|std::make_pair|' mecab/src/*.cpp

%build
%configure --with-hts-engine-header-path=/usr/include --with-hts-engine-library-path=%{_libdir} --with-charset=UTF-8
make %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}

%{__install} -m0755 -D -s bin/open_jtalk %{buildroot}/usr/bin/open_jtalk
cd mecab-naist-jdic
%define datadir %{buildroot}%{_datadir}/%{name} 
%{__install} -m0755 -d			%{datadir}/mecab-naist-jdic

/usr/bin/install -D -m 644 'matrix.bin'		%{datadir}/mecab-naist-jdic/matrix.bin
/usr/bin/install -D -m 644 'char.bin'		%{datadir}/mecab-naist-jdic/char.bin
/usr/bin/install -D -m 644 'sys.dic'		%{datadir}/mecab-naist-jdic/sys.dic
/usr/bin/install -D -m 644 'unk.dic'		%{datadir}/mecab-naist-jdic/unk.dic
/usr/bin/install -D -m 644 'left-id.def'	%{datadir}/mecab-naist-jdic/left-id.def
/usr/bin/install -D -m 644 'right-id.def'	%{datadir}/mecab-naist-jdic/right-id.def
/usr/bin/install -D -m 644 'rewrite.def'	%{datadir}/mecab-naist-jdic/rewrite.def
/usr/bin/install -D -m 644 'pos-id.def'		%{datadir}/mecab-naist-jdic/pos-id.def

cd ..
%define docdir %{buildroot}%{_docdir}/%{name}
%{__install} -m0755 -d			%{docdir}/
%{__install} -m0644 -D AUTHORS		%{docdir}/AUTHORS
%{__install} -m0644 -D COPYING		%{docdir}/COPYING
%{__install} -m0644 -D ChangeLog	%{docdir}/ChangeLog
%{__install} -m0644 -D NEWS		%{docdir}/NEWS
%{__install} -m0644 -D README		%{docdir}/README
%{__install} -m0644 -D mecab/COPYING	%{docdir}/mecab/COPYING

%clean
%{__rm} -rf %{buildroot}

%files
%{_bindir}/open_jtalk
%{_datadir}/%{name}/*
%{_docdir}/%{name}/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.05
- Rebuilt for Fedora
