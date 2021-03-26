%global debug_package %{nil}

Summary: Console hex editor
Name: heme
Version: 0.4.2
Release: 5.1
License: GPL
Group: Applications/Editors
URL: http://heme.sourceforge.net/
Source: http://dl.sf.net/heme/heme-%{version}.tar.gz
BuildRequires: ncurses-devel

%description
Heme is a fast and portable console hex editor. It has undo support, ability
to fill a range of addresses with the specified byte, ability to search for
a single byte or character string.

Offsets can be given in hexadecimal, octal or decimal. There are two editing
modes: hex and ascii. In hex mode you type hexadecimal digits and in ascii
mode you type characters. In ascii mode the cursor is automatically moved
to the next byte after typing a character.

%prep
%setup -q

%build 
export CFLAGS="%{optflags} -DHAVE_MMAP"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
#%{__make} install INSTALL_PREFIX="%{buildroot}%{_prefix}"
%{__install} -Dp -m0755 heme %{buildroot}%{_bindir}/heme
%{__install} -Dp -m0644 heme.1 %{buildroot}%{_mandir}/man1/heme.1

%clean
%{__rm} -rf %{buildroot}

%files
%doc COPYING INSTALL README THANKS
%{_mandir}/man1/heme.1*
%{_bindir}/heme

%changelog
* Tue Mar 31 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.2
- Rebuild for Fedora
* Sun Jan  3 2010 J. Randall Owens <jrowens@ghiapet.net> - 0.4.2-2
- rebuild for Fedora 12
* Mon Jan 29 2007 Dag Wieers <dag@wieers.com> - 0.4.2-1 - +/
- Initial package. (using DAR)
