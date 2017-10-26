
    ClassicEditor
        .create( document.querySelector( '#editor1' ) )
        .catch( error => {
            console.error( error );
        } );
    ClassicEditor
        .create( document.querySelector( '#editor2' ) )
        .catch( error => {
            console.error( error );
        } );
    ClassicEditor
        .create( document.querySelector( '#editor3' ) )
        .catch( error => {
            console.error( error );
        } );
    ClassicEditor
        .create( document.querySelector( '#editor4' ) )
        .catch( error => {
            console.error( error );
        } );
    ClassicEditor
        .create( document.querySelector( '#editor5' ) )
        .catch( error => {
            console.error( error );
        } );
    ClassicEditor
    .create( document.querySelector( '#editor_title' ), {
        toolbar: [ 'headings', 'bold', 'italic', '|', 'link', 'bulletedList', 'numberedList', 'blockQuote', ],
        heading: {
            options: [
                { modelElement: 'paragraph', title: 'Titulo 1', class: 'ck-heading_paragraph' },
                { modelElement: 'heading1', viewElement: 'h1', title: 'Titulo 2', class: 'ck-heading_heading1' },
                { modelElement: 'heading2', viewElement: 'h2', title: 'Titulo 3', class: 'ck-heading_heading2' },
                { modelElement: 'heading3', viewElement: 'h3', title: 'Titulo 4', class: 'ck-heading_heading3' },
                { modelElement: 'heading4', viewElement: 'h4', title: 'Titulo 5', class: 'ck-heading_heading4' },
                { modelElement: 'heading5', viewElement: 'h5', title: 'Titulo 6', class: 'ck-heading_heading5' }
            ]
        }
    } )
    .catch( error => {
        console.log( error );
    } );