%define name comix
%define version 4.0.3
%define summary Comic book viewer

Summary: %summary
Name: %name
Version: %version
Release: %mkrel 2
License: GPLv2+
Group: Office
URL: http://comix.sourceforge.net/
Source: http://downloads.sourceforge.net/comix/%name-%{version}.tar.gz
Source1: %name-icons.tar.bz2
Patch0: comix-4.0.0-disable-update-mime-db.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Buildarch: noarch
BuildRequires: python, python-imaging, jpeg-progs, pygtk2.0
BuildRequires: desktop-file-utils
Requires: python, python-imaging, jpeg-progs, pygtk2.0


%description
Comix is a comic book viewer. It reads zip, rar, tar, tar.gz, and tar.bz2
archives (often called .cbz, .cbr and .cbt) as well as normal image files.

%prep
%setup -q -n %{name}-%{version} -a1
%patch0 -p0

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}%{_prefix}
%{__python} install.py install --dir %{buildroot}%{_prefix}

%find_lang %{name} --with-gnome

desktop-file-install --vendor='' \
	--dir %buildroot%_datadir/applications \
	--remove-category='Application' \
	--add-category='GNOME;GTK' \
	%buildroot%_datadir/applications/*.desktop

%post
%{update_desktop_database}
%{update_mime_database}

%postun
%{clean_desktop_database}
%{clean_mime_database}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root)
%doc ChangeLog COPYING README
%{_bindir}/comicthumb
%{_bindir}/comix
%{_datadir}/comix
%{_mandir}/man1/*
%{_datadir}/applications/*comix.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/mime/packages/comix.xml
