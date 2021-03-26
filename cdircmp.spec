Name:			cdircmp
Summary:		Compare directories and select files to copy
Version:		0.3
Release:		4.1
Group:			Productivity/File utilities
License:		GPL
Source:			%{name}-%{version}.tar.gz
URL:			http://home.hccnet.nl/paul.schuurmans/linux/index.html#xdircmp
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Patch0:			%{name}-%{version}-ncurses.patch
BuildRequires:		ncurses-devel

%description
This is a simple utitlty that compares two directories, displays the
differences and allows you to select items to copy. This is mainly
for the purpose of keeping backup directories up-to-date.

%prep
%setup -q
##%patch0

%build
%{__make} CFLAGS="$RPM_OPT_FLAGS"

%install
%{__rm} -rf $RPM_BUILD_ROOT
install -D -m755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%files
%defattr(-,root,root,0755)
%{_bindir}/%{name}
%doc AUTHORS ChangeLog COPYING README

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%changelog
* Tue Aug 07 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3
- Rebuild for Fedora
* Fri Jan 27 2006 David Bolt <davjam@davjam.org>
- First spec and build for SUSE.
