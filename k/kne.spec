%global debug_package %{nil}

Name: kne
Summary: ISPF xedit compitable editor
Version: 3.0
Release: 15.1
Group: Applications/Editors
License: GPL
URL: http://www.pm9.com/kne_ind.html
Source0: http://www.pm9.com/KNE-30.tar.gz
Conflicts: the
BuildRequires: ncurses-devel
BuildRequires: regina-devel

%description
KNE is based on "THE"-Editor on UN*X(include LINUX). It is very easy for
Japanese user with the Kanji-handling function - written by Kunimasa Noda.
And, It is also intended to be similar to the VM/CMS System Product Editor,
ISPF XEDIT and KEDIT.

%prep
%setup -q -n KNE-%{version}
%ifarch x86_64 aarch64
sed -i 's|/usr/lib|/usr/lib64|' configure
%endif

%build
./configure \
	--prefix=/usr \
	--mandir=%{_mandir} \
	--with-ncurses \
	--with-rexx=regina
make

%install
make install prefix=%{buildroot}/usr/share
mv %{buildroot}/usr/share/bin %{buildroot}/usr/bin

%files
%doc demo.txt TODO HISTORY FAQ README COPYING
%{_bindir}/%{name}
%{_datadir}/THE/*

%changelog
* Sun Jun 23 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 3.0
- Rebuilt for Fedora
