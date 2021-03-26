%global debug_package %{nil}

Name:		bibshelf
Version:	1.6.0
Release:	10.1
License:	GNU GPL v2
Group:		Productivity/Office/Organizers
URL:		http://code.google.com/p/bibshelf/
Source:		%{name}-%{version}.tar.bz2
Patch1:		bibshelf-sigc_namespace-1.6.0.patch
Patch2:		bibshelf-bibshelf.desktop.in.in-1.6.0.patch
BuildRequires:	gcc-c++ gtkmm24-devel intltool libcurl-devel libglademm24-devel libxml++-devel desktop-file-utils
Summary:	A book organizer

%description
BibShelf is a book organizer integrating well with the GNOME desktop environment.

%prep
%setup -q
%patch1 -p1
%patch2 -p1

%build
export CXXFLAGS="-O2 -std=c++11 -fPIC"
%configure
%__make %{?jobs:-j%jobs}

%install
%__rm -rf $RPM_BUILD_ROOT
%makeinstall
%find_lang %name

%clean
%__rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%doc AUTHORS ChangeLog
%{_bindir}/bibshelf
%exclude /usr/doc/bibshelf
%{_datadir}/applications/bibshelf.desktop
%{_datadir}/bibshelf

%changelog
* Tue Aug 21 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.6.0
- Rebuild for Fedora
* Wed Jan 21 2009 bitshuffler #suse@irc.freenode.org
- Initial RPM
