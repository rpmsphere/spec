Name:      abc2prt
Version:   1.0.2
Release:   3.1
Summary:   A program to extract parts from multivoice ABC files
License:   GPL
URL:       https://abcplus.sourceforge.net
Group:     Applications/File
Source:    https://abcplus.sourceforge.net/%{name}-%{version}.tar.gz

%description
abc2prt is a simple program to extract parts from multivoice ABC music files.

%prep
%setup -q

%build
make CFLAGS="$RPM_OPT_FLAGS -Wall"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/abc2prt
%{_bindir}/install -m 755 abc2prt $RPM_BUILD_ROOT%{_bindir}

%files
%doc COPYING INSTALL README
%{_bindir}/*

%changelog
* Mon Mar 30 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.2
- Rebuilt for Fedora
