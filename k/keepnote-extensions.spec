Name:           keepnote-extensions
Version:        0
Release:        6.2
License:        GPL-2.0
Summary:        KeepNote Extensions
URL:            https://keepnote.org/extensions.shtml
Group:          Productivity/Office/Organizers
Source0:        https://raw.github.com/mdrasmus/keepnote-extensions/master/stable/import_basket.kne
Source1:        https://raw.github.com/mdrasmus/keepnote-extensions/master/stable/import_folders.kne
Source2:        https://raw.github.com/mdrasmus/keepnote-extensions/master/stable/import_notecase.kne
Source3:        https://raw.github.com/mdrasmus/keepnote-extensions/master/stable/import_txt.kne
Source4:        https://raw.github.com/mdrasmus/keepnote-extensions/master/stable/make_catalog.kne
BuildRequires:  unzip
Requires:       keepnote
BuildArch:      noarch

%description
Additional extensions for KeepNote organizer.
The package includes:
* Import Basket
    Primitive import of Basket Notepad Databases.
* Import Folder Tree
    Imports a folder tree as nodes in a notebook
* Import NoteCase
    Primitive import of NoteCase .ncd Files
* Import Plain Text
    Imports plain text files as nodes in a notebook
* Make File Catalog
    Imports a folder tree, listing file names (maybe as links) notebook.

%prep

%build

%install
install -dm 0755 $RPM_BUILD_ROOT%{python2_sitelib}/keepnote/extensions
unzip -q "%{_sourcedir}/*.kne" -d \
    $RPM_BUILD_ROOT%{python2_sitelib}/keepnote/extensions
# Remove backup file.
rm -f \
    $RPM_BUILD_ROOT%{python2_sitelib}/keepnote/extensions/import_basket/#__init__.py#
cd $RPM_BUILD_ROOT%{python2_sitelib}/keepnote/extensions

%files
%{python2_sitelib}/keepnote/extensions/*

%changelog
* Sun Sep 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0
- Rebuilt for Fedora
* Sun Nov 13 2011 lazy.kent@opensuse.org
- Initial package created.
