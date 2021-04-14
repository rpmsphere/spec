Name:			gdircmp
Summary:		Compare directories and select files to copy
Version:		0.8
Release:		14.1
Group:			Productivity/File utilities
License:		GPL
Source:			%{name}-%{version}.tar.gz
URL:			http://home.hccnet.nl/paul.schuurmans/linux/index.html#xdircmp
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:		gtk2-devel
BuildRequires:		libX11-devel

%description
This is a simple utitlty that compares two directories, displays the
differences and allows you to select items to copy. This is mainly
for the purpose of keeping backup directories up-to-date.

%prep
%setup -q

%build
./autogen.sh
%configure
make CFLAGS="$RPM_OPT_FLAGS"

%install
%{__rm} -rf $RPM_BUILD_ROOT
install -D -m755 src/%{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%changelog
* Wed Aug 01 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8
- Rebuilt for Fedora
* Fri Jan 27 2006 David Bolt <davjam@davjam.org> 0.7
- First spec and build for SUSE.
