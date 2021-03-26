Name:           xiangchi
Version:        0.1
Release:        15.1
Summary:        Console Chinese Chess Board
License:        GPL
URL:            http://sourceforge.net/projects/xiangchi/
Source0:        http://sourceforge.net/projects/xiangchi/files/xiangchi/xiangchi-0.1/xiangchi-0.1.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:  gcc-c++

%description
Xiang Chi, also known as xiang-qi, is an ancient game similar to European chess.
This project runs in a terminal an interacts via stdin/stdour. The design allows
a GUI frontend to be placed over it as well as programs that enable network play.

%prep
%setup -q -n %{name}
sed -i '21i #include <cstring>\n#include <cstdlib>' types.h
sed -i '18i #include <cstdio>' iomodule.cc player.cc

%build
make depend
make

%install
rm -rf $RPM_BUILD_ROOT
install -Dm755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%files
%doc README COPYING
%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sun Oct 21 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1
- Rebuild for Fedora
