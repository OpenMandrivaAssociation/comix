Summary: Comic book viewer
Name:    comix
Version: 4.0.4
Release: 4
License: GPLv2+
Group:   Office
URL:     http://comix.sourceforge.net/
Source:  http://downloads.sourceforge.net/comix/%{name}-%{version}.tar.gz
Patch0:  comix-4.0.0-disable-update-mime-db.patch
Patch2:  comix-4.0.4-import-PIL-for-Image.patch

Buildarch: noarch
BuildRequires: python
BuildRequires: python-pillow
BuildRequires: jpeg-progs
BuildRequires: pygtk2.0
BuildRequires: desktop-file-utils
Requires: python
Requires: python-imaging
Requires: jpeg-progs
Requires: pygtk2.0


%description
Comix is a comic book viewer. It reads zip, rar, tar, tar.gz, and tar.bz2
archives (often called .cbz, .cbr and .cbt) as well as normal image files.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p0
%patch2 -p1 -b .pil

%build

%install
%{__install} -d %{buildroot}%{_prefix}
python install.py install --dir %{buildroot}%{_prefix}

%find_lang %{name} --with-gnome

desktop-file-install --vendor='' \
	--dir %{buildroot}%{_datadir}/applications \
	--remove-category='Application' \
	--add-category='GNOME;GTK' \
	%{buildroot}%{_datadir}/applications/*.desktop

%post
%{update_desktop_database}
%{update_mime_database}

%postun
%{clean_desktop_database}
%{clean_mime_database}

%clean

%files -f %{name}.lang
%doc ChangeLog COPYING README
%{_bindir}/comicthumb
%{_bindir}/comix
%{_datadir}/comix
%{_mandir}/man1/*
%{_datadir}/applications/*comix.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/mime/packages/comix.xml


